
import SwiftUI
import UIKit

struct RecipesView: View {
    
    //    var recipes: [Recipes] = []
    
    var body: some View {
        
        //DESIGN ---------------------------------
        VStack {
            RoundedRectangle(cornerRadius: 5.0)
                .fill(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255))
                .frame(width: 414, height: 115)
                .overlay(Text("Recipes")
                    .font(.custom("Hiragino Sans W3", size: 34))
                    .foregroundColor(.gray)
                    .offset(y: 15)
                    , alignment:
                    .center)
            
            HStack {
                Button(action: { print("All") }) {
                    Text("All Recipes")
                        .font(.custom("Hiragino Sans W3", size: 22))
                        .foregroundColor(.gray)
                        .padding(15)
                }
                Button(action: { print("Saved") }) {
                    Text("Saved Recipes")
                        .font(.custom("Hiragino Sans W3", size: 22))
                        .foregroundColor(.gray)
                        .padding(15)
                }
            }
            NavigationView {
                List(1...5, id: \.self) { index in
                    NavigationLink(
                        destination: Text("Food Item #\(index) Details"),
                        label: {
                            Text("Food Item #\(index)")
                                .font(.custom("Hiragino Sans W3", size: 22))
                                .foregroundColor(.gray)
                    })
                }
            }
//            .offset(y: -)
            
            Spacer()
        }
    }
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            RecipesView()
        }
    }
    
    //    struct Recipe: View{
    //        var body: some View{
    //            NavigationLink(destination: Text(recipe.name)) {
    //                Image(recipe.thumbnailName)
    //                    .cornerRadius(5)
    //                Text(recipe.name)
    //            }
    //        }
    //    }
    
}
