
import SwiftUI
import UIKit

struct RecipesView: View {
    
    @State var recipes: [Recipes] = []
    
    var body: some View {
        VStack {
            
            RoundedRectangle(cornerRadius: 5.0)
                .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                .edgesIgnoringSafeArea(.top)
                .frame(width: 420, height: 50)
                .overlay(Text("Recipes")
                    .fontWeight(.regular)
                    .font(.custom("Hiragino Sans W3", size: 34))
                    .foregroundColor(.white)
                            .offset(y: -20)
                    , alignment:
                    .center)
                
            HStack(spacing:30) {
               
                Button(action: { Api().getRecipeDetails { (recipes) in
                    self.recipes = recipes
                } })  {
                    Text("All Recipes")
                        .font(.custom("Hiragino Sans W3", size: 20))
                        .foregroundColor(.gray)
                        .frame(width: 160, height: 50)
                    
                }.buttonStyle(PrimaryButtonStyle())
                .overlay(
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)
                )
                .padding(.top)
                
                Button(action: { print("Saved") }) {
                    Text("Saved Recipes")
                        .font(.custom("Hiragino Sans W3", size: 20))
                        .foregroundColor(.gray)
                        .frame(width: 160, height: 50)
                    
                }.buttonStyle(PrimaryButtonStyle())
                .overlay(
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)
                )
                .padding(.top)
            }
                
            List(recipes) { recipe in
                NavigationLink(destination: RecipeDetails(recipe: recipe)) {
                    RecipeRow(recipe: recipe)
                }
            }.onAppear {
                Api().getRecipeDetails { (recipes) in
                    self.recipes = recipes
                }
            }

            Button(action: { Api().getRecipeDetails { (recipes) in
                self.recipes = recipes
            } }) {
                Text("GENERATE NEW RECIPES")
                    .frame(width: 260, height: 20)
                    .padding()
                    .font(.custom("Hiragino Sans W3", size: 18))
                    .foregroundColor(.gray)
                    .multilineTextAlignment(.center)
            }
            .buttonStyle(PrimaryButtonStyle())
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)
            )
            .padding(.bottom)
        }
    }
}

struct RecpiesView_Previews: PreviewProvider {
    static var previews: some View {
        RecipesView()
            .background(Color(.systemBackground))
            .edgesIgnoringSafeArea(.top)
    }
}

struct PrimaryButtonStyle: ButtonStyle {
    func makeBody(configuration: Self.Configuration) -> some View {
        configuration.label
            .foregroundColor(.white)
            .background(configuration.isPressed ? Color(.systemGray5) : Color.white)
    }
}


