import SwiftUI
import UIKit

struct RecipeDetails: View {

  //  var recipe: Recipes
    @State var recipes: [Recipes] = []
    
//        .onAppear(){
//            Api().getRecipeDetails { (recipes) in
//                self.recipes = recipes
//            }
//        }

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
                    .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                    .frame(width: 414, height: 100)
                
                HStack {
                    Image(recipes[0].image)
                        .resizable()
                        .aspectRatio(contentMode: .fill)
                        .frame(width: 145, height: 145)
                        .clipped()
                        .cornerRadius(150)
                        .shadow(radius: 3)
                    Spacer()
                    VStack(alignment: .leading) {
                        Text(recipes[1].name)
                            .font(.custom("Hiragino Sans W3", size: 25))
                            .fontWeight(.heavy)
                            .foregroundColor(.black)
                        Text("Cuisine: " + recipes[2].cuisine)
                            .font(.custom("Hiragino Sans W3", size: 20))
                            .foregroundColor(.black)
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
                    Text(recipes[3].ingredients)
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
                    Text(recipes[4].insructions)
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
            RecipeDetails(recipes: [])
        }
}

