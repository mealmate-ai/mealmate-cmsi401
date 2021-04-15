
import SwiftUI

struct RecipesView: View {
    
    //    @State var buttonTapped: Bool = false
    //    var recipes: [Recipes] = []
    
    var body: some View {
        //DESIGN ---------------------------------
        NavigationView {
            VStack {
                RoundedRectangle(cornerRadius: 5.0)
                    .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                    .frame(width: 419, height: 120)
                    .overlay(Text("Recipes")
                                .font(.custom("Hiragino Sans W3", size: 34))
                                .foregroundColor(.white)
                             , alignment:
                                .center)
                
                HStack(spacing:30) {
                    Button(action: { print("All") })  {
                        Text("All Recipes")
                            .font(.custom("Hiragino Sans W3", size: 20))
                            .foregroundColor(.gray)
                            .frame(width: 160, height: 50)
                        
                    }.buttonStyle(PrimaryButtonStyle())
                    .overlay(
                        RoundedRectangle(cornerRadius: 15)
                            .stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)
                    )
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
                }
                
                //  NavigationView {
                List(recipes) { recipe in
                    NavigationLink(destination: RecipeDetails(recipe: recipe)) {
                        RecipeRow(recipe: recipe)
                    }
                }
                //            }
                //            .navigationBarTitle("")
                //            .navigationBarHidden(true)
                //            .padding(10)
                
                Button(action: { print("Generate Recipes") }) {
                    Text("GENERATE NEW RECIPES")
                        .frame(width: 260, height: 20)
                        .padding()
                        .font(.custom("Hiragino Sans W3", size: 18))
                        .foregroundColor(.gray)
                        .multilineTextAlignment(.center)
                }.buttonStyle(PrimaryButtonStyle())
                .overlay(
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)
                )
            }
            .navigationBarTitle("")
            .navigationBarHidden(true)
            
            
            Spacer()
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
}

