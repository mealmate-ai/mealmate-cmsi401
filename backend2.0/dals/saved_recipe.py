from sqlalchemy.exc import IntegrityError
from dals.models import db, SavedRecipe, Recipe
from apis.spoonacular import spoonacular


def insert_saved_recipe(recipe_details):
    try:
        new_saved_recipe = SavedRecipe(**recipe_details)
        db.session.add(new_saved_recipe)
        db.session.commit()

        return new_saved_recipe.full_view()
    except IntegrityError:
        db.session.rollback()
        return None
    except Exception:
        db.session.rollback()
        raise


def get_recipes_list(account_id):
    recipes = SavedRecipe.get_saved_recipes_by_user(account_id)
    return [Recipe.get_recipe_by_id(recipe.recipe_id).full_view() for recipe in recipes]


def spoonacular_recipes_list(account_id):
    recipes = SavedRecipe.get_saved_recipes_by_user(account_id)
    ids = [str(r.recipe_id) for r in recipes]
    if len(ids) > 0:
        try:
            return [
                {
                    'id': res['id'],
                    'title': res['title'],
                    'image': res['image'] if res['image'] else '',
                    'cuisine': ' '.join(res['cuisines']),
                    'liked': True,
                    # 'instructions': res['instructions'],
                    'ingredients': [
                        ' '.join(
                            [
                                str(ing['measures']['us']['amount']),
                                ing['measures']['us']['unitShort'],
                                ing['name'],
                            ]
                        )
                        for ing in res['extendedIngredients']
                    ],
                }
                for res in spoonacular.recipe_information_bulk(ids)
            ]
            
        except Exception:
            raise
    else:
        return []