//
//  Recipes.swift
//  Daily Bites
//
//  Created by Maya Dahlke on 3/17/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//

import Foundation
import SwiftUI

struct Recipes: Codable, Identifiable {
    let id: Int
    let title: String
    let image: String
    let cuisine: String
    let liked: Bool
//    let nutrients: String
    let ingredients: [String]
//    let insructions: String

}


struct ApiResponse: Codable {
    let recipes: [Recipes]
}

var token: String = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MTk2NDU5NDAsImlhdCI6MTYxOTY0MzI0MCwic3ViIjoiOWY0MzdhYTgtNjhiNC00ZTAwLWI3YTEtYmYwNTRhNTg1OTRhIn0.ZIg4rF6pvtW0pGofIu0fuXFzkJfHgBBtysi1rn9IYeg"

class Api{
    func getRecipeDetails(completion: @escaping ([Recipes]) -> ()) {
       guard let url = URL(string: "http://0.0.0.0:8080/recipes")
       else {return}
        
        var request = URLRequest(url: url)
        request.setValue( "Bearer \(token)", forHTTPHeaderField: "Authorization")
        request.httpMethod = "GET"
    
        
        URLSession.shared.dataTask(with: request) { (data, _, _) in
            print("Data", data!)
            let recipeDetails = try! JSONDecoder().decode(ApiResponse.self, from:data!)
            print("Recipe Details: ", recipeDetails)
            
            DispatchQueue.main.async {
                completion(recipeDetails.recipes)
            }
        }
        .resume()
    }
    
    func getSavedRecipes(completion: @escaping ([Recipes]) -> ()) {
        guard let url = URL(string: "http://0.0.0.0:8080/saved-recipes")
        else {return}
        
        var request = URLRequest(url: url)
        request.setValue( "Bearer \(token)", forHTTPHeaderField: "Authorization")
        request.httpMethod = "GET"
        
        URLSession.shared.dataTask(with: request) { (data, _, _) in
            print("Data", data!)
            let savedRecipes = try! JSONDecoder().decode(ApiResponse.self, from:data!)
            print("Recipe Details: ", savedRecipes)
            
            DispatchQueue.main.async {
                completion(savedRecipes.recipes)
            }
        }
        .resume()
    }
}

//let recipes = [
//    Recipes(image: "greeksalad", name: "Greek Side Salad", cuisine: "Greek", liked: false, ingredients: "1.0 large cucumber, 4.0 servings extra virgin olive oil, 0.25 pound feta, 12.0 kalamata olives, 1.0 large red onion, 5.0 large tomatoes", insructions: "1) Slice the vegetables into bite-size wedges. 2) Toss in a bowl with olive oil, 3) Place feta on top of the salad or break up into crumbles"),
//    Recipes(image: "ratatouille", name: "Vegetarian Ratatouille", cuisine: "French", liked: true, ingredients: "1.0 eggplant, 1.0 zucchini, 1.0 yellow squash, 2.0 tomato, 0.5 red bell pepper, 0.5 orange bell pepper, 1 onion, 5.0 cloves garlic, 2.0 Tbsps fresh basil, 2.0 sprigs thyme, 0.25 dried oregano tsps, 2.0 Tbsps extra virgin olive oil, 1.0 tsp sea salt", insructions: "1) Saute onion and garlic in a large saucepan over medium low heat until onions are translucent. 2) Add tomatoes and stir. 3) Add all the remaining ingredients and cook for 30 minutes on low stirring occasionally or until eggplant is tender."),
//    Recipes(image: "perillapesto", name: "Korean Perilla Pesto", cuisine: "Korean", liked: false, ingredients: "1.0 fresh sesame, 0.5 cup dry pine nuts, 2.0 Tbsps garlic, 0.75 cup canned extra-virgin olive oil, 0.5 tsps salt, 0.25 tsps black pepper", insructions: "1) Put all the ingredients into a food processor and blend everything until it is a smooth paste. 2) Toss it in a bowl with some freshly cooked pasta of your choice and serve, garnishing with some leftover pine nuts."),
//    Recipes(image: "japanesesalad", name: "Japanese Cucumber Salad", cuisine: "Japanese", liked: false, ingredients: "1.0 english cucumber, 3.0 green onions, 1.0 Tbsp rice wine vinegar, 1.0 tsp sesame oil, 2.0 tsps soy sauce, 0.25 sugar", insructions: "1) Combine all ingredients in a large bowl; toss until combined.This recipe yields 4 servings.Comments: Try to purchase English, a.k.a., seedless cucumbers, instead of regular ones. Though not actually seedless, the seeds are smaller and the flesh firmer.Description: This light, refreshing salad is a perfect accompaniment to grilled or roasted meats."),
//    Recipes(image: "thaisalad", name: "Thai Sausage Salad", cuisine: "Thai", liked: false, ingredients: "6.0 sausages, 2.0 large cucumbers, 1.0 cup fresh bean sprouts, 4.0 green onions, 1.0 leaf fresh cilantro leaves, 1.0 fresh red chili pepper, 1.0 searving cooked jasmine rice, 0.5 cup fresh lime juice, 3.0 tsps granulated sugar, 2.0 Tbsps thai fish sauce, 1.0 tsp soy sauce", insructions: "1) In a small bowl, combine the dressing ingredients and stir until the sugar has dissolved. Taste and adjust with more sugar or fish sauce if needed (some limes are more tart than others). Set aside. 2) Slice the sausage thinly on the diagonal. 3) Place in a non stick skillet over medium heat and saut until the edges are slightly browned and sausage is cooked thru, about 5 minutes. Dont over cook. Set aside to cool. 4) Peel the cucumbers, slice thinly and place in a large bowl. Thinly slice the green onions on the diagonal and add to the bowl. 5) Add the bean sprouts, cooked sausage and the dressing. Lightly toss and serve on plates with jasmine rice on the same plate. 6) Garnish with a few slivers of sliced hot chili pepper, if desired, and a few leaves of fresh parsley or cilantro. 7) Serves 2 as a main course salad.")
//]



struct Recipes_Previews: PreviewProvider {
    static var previews: some View {
        /*@START_MENU_TOKEN@*/Text("Hello, World!")/*@END_MENU_TOKEN@*/
    }
}
