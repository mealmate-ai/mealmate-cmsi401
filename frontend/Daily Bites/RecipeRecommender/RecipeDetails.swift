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
