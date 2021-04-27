import SwiftUI
import UIKit

struct RecipeDetails: View {

    @State var recipe: Recipes
    @State var isFavorite =  false
    
    var body: some View {

        VStack {
        
            HStack {
                Spacer()
                Button(action: {
                    print("You liked this recipe")
                    isFavorite = !self.isFavorite
                }) {
                    if isFavorite {
                        Image(systemName: "heart.fill")
                            .foregroundColor(.red)
                    } else {
                        Image(systemName: "heart.fill")
                            .foregroundColor(.gray)
                    }
                }
                .font(.system(size:30))
                .padding(.trailing, 30)
            }
        
            ZStack {
                RoundedRectangle(cornerRadius: 5.0)
                    .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                    .frame(width: 414, height: 100)
        
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
                        Text(recipe.title)
                            .font(.custom("Hiragino Sans W3", size: 25))
                            .fontWeight(.heavy)
                            .foregroundColor(.black)
                        Text("Cuisine: " + recipe.cuisine)
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
                    Text(recipe.insructions)
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
                    Text(recipe.ingredients)
                        .font(.custom("Hiragino Sans W3", size: 15))
                        .foregroundColor(.gray)
                }.padding(15)
            }
            
            HStack {
                VStack(alignment: .leading, spacing: 15) {
                    Text("Instructions")
                        .font(.custom("Hiragino Sans W3", size: 20))
                        .foregroundColor(.gray)
                        .fontWeight(.medium)
                    Text(recipe.nutrients)
                        .font(.custom("Hiragino Sans W3", size: 15))
                        .foregroundColor(.gray)
                }.padding(15)
            }
        
            Spacer()
        
        }

    }
}

//struct RecipeDetails_Previews: PreviewProvider {
//    static var previews: some View {
//        RecipeDetails(recipe: <#Recipes#>)
//    }
//}
//

