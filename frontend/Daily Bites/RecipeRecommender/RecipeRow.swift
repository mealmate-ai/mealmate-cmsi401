//
//  RecipeRow.swift
//  Daily Bites
//
//  Created by Maya Dahlke on 3/17/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//

import SwiftUI

struct RecipeRow: View {
    
    let recipe: Recipes
    
    var body: some View {
        HStack {
            Image(recipe.image)
                .resizable()
                .aspectRatio(contentMode: .fill)
                .frame(width: 60, height: 60)
                .clipped()
                .cornerRadius(50)
            VStack(alignment: .leading) {
                Text(recipe.name)
                    .font(.custom("Hiragino Sans W3", size: 22))
                    .foregroundColor(.gray)
            }
        }
    }
}

struct RecipeRow_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            RecipeRow(recipe: recipes[0])
            RecipeRow(recipe: recipes[1])
        }
    }
}
