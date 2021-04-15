<<<<<<< HEAD
//import SwiftUI
//import UIKit
//
//struct RecipeDetails: View {
//
////    var recipe: Recipe
//
//    var body: some View {
//
//        VStack{
//            RoundedRectangle(cornerRadius: 5.0)
//                .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
//                .frame(width: 419, height: 120)
//                .overlay(Text("Trends")
//                .fontWeight(.regular)
//                .font(.custom("Hiragino Sans W3", size: 34))
//                .foregroundColor(.white)
//                         , alignment:
//                            .center)
//
//            HStack{
//                Image("recipe.imageName")
//                    .resizable()
//                VStack{
//                    HStack{
//                        Text("recipe.name")
////                        Image(systemName: onCLick ? "heart" : "heart.fill")
////figure out how to add to saved when heart is filled
//                    }
//                    Text("meal.type")
//                    Text("cuisine.type")
//                }
//            }
//            VStack{
//                Text("Nutritional Information")
//                Text("calories")
//                Text("fat")
//                Text("carbs")
//                Text("protein")
//            }
//            VStack{
//                Text("Ingredients")
//                List{
//                    Text("ingredients")
//                }
//            }
//            VStack{
//                Text("Instructions")
//                List{
//                    Text("instructions")
//                }
//            }
//        }
//    }
//
//    struct ContentView_Previews: PreviewProvider {
//        static var previews: some View {
//            RecipeDetails(recipe:testData[0])
//            .background(Color(.systemBackground))
//        }
//    }
//}
=======
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
                        Text(recipe.name)
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

>>>>>>> bree-spring
