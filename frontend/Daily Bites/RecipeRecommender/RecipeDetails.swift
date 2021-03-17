import SwiftUI
import UIKit

struct RecipeDetails: View {

    var recipe: Recipes

    var body: some View {
        VStack {
            
            HStack {
                Spacer()
                Button(action: {
                    print("You liked this recipe")
                    //The button can change from filled to unfilled
                    //based on the Bool value of recipe.liked
                }) {
                    Image(systemName: "heart")
                }
                .font(.system(size:30))
                .padding(.trailing, 30)
            }
            
            ZStack {
                RoundedRectangle(cornerRadius: 5.0)
                    .fill(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255))
                    .frame(width: 414, height: 115)
                
                HStack {
                    Image(recipe.image)
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                        .frame(width: 145, height: 145)
                        .clipped()
                        .cornerRadius(150)
                        .shadow(radius: 3)
                    Spacer()
                    VStack(alignment: .leading) {
                        Text(recipe.name)
                            .font(.custom("Hiragino Sans W3", size: 25))
                            .fontWeight(.heavy)
                            .foregroundColor(.gray)
                        Text("Cuisine: " + recipe.cuisine)
                            .font(.custom("Hiragino Sans W3", size: 20))
                            .foregroundColor(.gray)
                    }
                }
                .padding(.leading, 35)
                .padding(.trailing, 35)
            }
            
            HStack {
                VStack(alignment: .leading, spacing: 15) {
                    Text("Ingredients")
                        .font(.custom("Hiragino Sans W3", size: 20))
                        .foregroundColor(.gray)
                        .fontWeight(.medium)
                    Text(recipe.ingredients)
                        .font(.custom("Hiragino Sans W3", size: 15))
                        .foregroundColor(.gray)
                        .lineLimit(10)
                }.padding(15)
            }
            
            
            HStack {
                VStack(alignment: .leading, spacing: 15) {
                    Text("Instructions")
                        .font(.custom("Hiragino Sans W3", size: 20))
                        .foregroundColor(.gray)
                        .fontWeight(.medium)
                    Text(recipe.insructions)
                        .font(.custom("Hiragino Sans W3", size: 15))
                        .foregroundColor(.gray)
                }.padding(15)
            }
           
            Spacer()
            
        }
    }
}
    struct RecipeDetails_Previews: PreviewProvider {
        static var previews: some View {
            RecipeDetails(recipe: recipes[4])
        }
}

