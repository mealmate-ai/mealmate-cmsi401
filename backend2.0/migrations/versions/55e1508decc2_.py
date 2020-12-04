"""empty message

Revision ID: 55e1508decc2
Revises: 
Create Date: 2020-12-04 11:05:34.357721

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '55e1508decc2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('date_created', sa.Date(), nullable=True),
        sa.Column('name', sa.String(length=128), nullable=True),
        sa.Column('email', sa.String(length=256), nullable=True),
        sa.Column('diets', sa.Text(), nullable=True),
        sa.Column('dietary_restrictions', sa.Text(), nullable=True),
        sa.Column('cuisine_preferences', sa.Text(), nullable=True),
        sa.Column('fbid', sa.String(length=128), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'nut_per_100_gram',
        sa.Column('food_id', sa.String(length=36), nullable=False),
        sa.Column('kcal', sa.Float(), nullable=True),
        sa.Column('protein_g', sa.Float(), nullable=True),
        sa.Column('total_fat_g', sa.Float(), nullable=True),
        sa.Column('total_carb_g', sa.Float(), nullable=True),
        sa.Column('total_diet_fiber_g', sa.Float(), nullable=True),
        sa.Column('calcium_mg', sa.Float(), nullable=True),
        sa.Column('iron_mg', sa.Float(), nullable=True),
        sa.Column('magnesium_mg', sa.Float(), nullable=True),
        sa.Column('phosphorus_mg', sa.Float(), nullable=True),
        sa.Column('potassium_mg', sa.Float(), nullable=True),
        sa.Column('sodium_mg', sa.Float(), nullable=True),
        sa.Column('zinc_mg', sa.Float(), nullable=True),
        sa.Column('copper_mg', sa.Float(), nullable=True),
        sa.Column('manganese_mg', sa.Float(), nullable=True),
        sa.Column('selenium_mcg', sa.Float(), nullable=True),
        sa.Column('vitamin_c_mg', sa.Float(), nullable=True),
        sa.Column('thiamin_mg', sa.Float(), nullable=True),
        sa.Column('riboflavin_mg', sa.Float(), nullable=True),
        sa.Column('niacin_mg', sa.Float(), nullable=True),
        sa.Column('pantothenic_acid_mg', sa.Float(), nullable=True),
        sa.Column('vitamin_b6_mg', sa.Float(), nullable=True),
        sa.Column('total_folate_mcg', sa.Float(), nullable=True),
        sa.Column('vitamin_b12_mcg', sa.Float(), nullable=True),
        sa.Column('vitamin_d_mcg', sa.Float(), nullable=True),
        sa.Column('vitamin_e_mg', sa.Float(), nullable=True),
        sa.Column('vitamin_k_mcg', sa.Float(), nullable=True),
        sa.Column('total_sat_fat_g', sa.Float(), nullable=True),
        sa.Column('total_monounsat_fat_g', sa.Float(), nullable=True),
        sa.Column('total_poly_unsat_fat_g', sa.Float(), nullable=True),
        sa.Column('total_trans_fat_g', sa.Float(), nullable=True),
        sa.Column('cholesterol_mg', sa.Float(), nullable=True),
        sa.Column('total_sugar_g', sa.Float(), nullable=True),
        sa.Column('omega_3_fatty_acids_g', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('food_id'),
    )
    op.create_table(
        'recipe',
        sa.Column('recipe_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=256), nullable=True),
        sa.Column('recipe_desc', sa.Text(), nullable=True),
        sa.Column('recipe_ingredients', sa.Text(), nullable=True),
        sa.Column('recipe_instructions', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('recipe_id'),
    )
    op.create_table(
        'food_detail',
        sa.Column('food_id', sa.String(length=36), nullable=False),
        sa.Column('food_desc', sa.String(length=256), nullable=True),
        sa.Column('barcode', sa.String(length=50), nullable=True),
        sa.Column('brand', sa.String(length=256), nullable=True),
        sa.ForeignKeyConstraint(
            ['food_id'],
            ['nut_per_100_gram.food_id'],
        ),
        sa.PrimaryKeyConstraint('food_id'),
    )
    op.create_index(
        op.f('ix_food_detail_food_desc'),
        'food_detail',
        [sa.text('to_tsvector(\'english\'::regconfig, "food_desc")')],
        postgresql_using='gin',
    )
    op.create_table(
        'food_unit',
        sa.Column('food_id', sa.String(length=36), nullable=False),
        sa.Column('unit_desc', sa.String(length=256), nullable=False),
        sa.Column('grams_per_unit', sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(
            ['food_id'],
            ['nut_per_100_gram.food_id'],
        ),
        sa.PrimaryKeyConstraint('food_id', 'unit_desc'),
    )
    op.create_table(
        'meal',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('account_id', sa.String(length=36), nullable=True),
        sa.Column('date_logged', sa.Date(), nullable=True),
        sa.Column('category', sa.String(length=15), nullable=True),
        sa.ForeignKeyConstraint(
            ['account_id'],
            ['account.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'saved_recipe',
        sa.Column('recipe_id', sa.Integer(), nullable=False),
        sa.Column('account_id', sa.String(length=36), nullable=False),
        sa.Column('date_saved', sa.Date(), nullable=True),
        sa.ForeignKeyConstraint(
            ['account_id'],
            ['account.id'],
        ),
        sa.ForeignKeyConstraint(
            ['recipe_id'],
            ['recipe.recipe_id'],
        ),
        sa.PrimaryKeyConstraint('recipe_id', 'account_id'),
    )
    op.create_table(
        'user_session',
        sa.Column('session_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('account_id', sa.String(length=36), nullable=True),
        sa.Column('date', sa.Date(), nullable=True),
        sa.Column('time_started', sa.DateTime(), nullable=True),
        sa.Column('time_completed', sa.DateTime(), nullable=True),
        sa.Column('num_clicks', sa.Integer(), nullable=True),
        sa.Column('screens_visited', sa.Date(), nullable=True),
        sa.Column('logged_meal', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ['account_id'],
            ['account.id'],
        ),
        sa.PrimaryKeyConstraint('session_id'),
    )
    op.create_table(
        'food',
        sa.Column('meal_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('food_id', sa.String(length=36), nullable=False),
        sa.Column('log_id', sa.Integer(), nullable=True),
        sa.Column('food_unit', sa.String(length=256), nullable=True),
        sa.Column('food_quantity', sa.String(length=256), nullable=True),
        sa.ForeignKeyConstraint(
            ['food_id'],
            ['nut_per_100_gram.food_id'],
        ),
        sa.ForeignKeyConstraint(
            ['meal_id'],
            ['meal.id'],
        ),
        sa.PrimaryKeyConstraint('meal_id', 'food_id'),
    )
    op.create_table(
        'meal_log',
        sa.Column('meal_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('log_id', sa.Integer(), nullable=False),
        sa.Column('raw_text', sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ['meal_id'],
            ['meal.id'],
        ),
        sa.PrimaryKeyConstraint('meal_id', 'log_id'),
    )


def downgrade():
    op.drop_table('meal_log')
    op.drop_table('food')
    op.drop_table('user_session')
    op.drop_table('saved_recipe')
    op.drop_table('meal')
    op.drop_table('food_unit')
    op.drop_table('food_detail')
    op.drop_table('recipe')
    op.drop_table('nut_per_100_gram')
    op.drop_table('account')
