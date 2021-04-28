//
//  RecipeRow.swift
//  Daily Bites
//
//  Created by Maya Dahlke on 3/17/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//

import SwiftUI

struct RecipeRow: View {
    
    @State var recipe: Recipes

    var body: some View {
        
        Text(recipe.title)
       
//        HStack {
//            Image($recipe.title)
//                .resizable()
//                .aspectRatio(contentMode: .fill)
//                .frame(width: 60, height: 60)
//                .clipped()
//                .cornerRadius(50)
//            VStack(alignment: .leading) {
//                Text($recipe.title)
//                    .font(.custom("Hiragino Sans W3", size: 20))
//                    .foregroundColor(.gray)
//            }
//        }
    }
}

 //struct RecipeRow_Previews: PreviewProvider {
 //    static var previews: some View {
 //        Group {
 //            RecipeRow(recipe: recipe[0])
 //            RecipeRow(recipe: recipe[1])
 //        }
 //    }
 //}
