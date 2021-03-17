
import SwiftUI
import UIKit

struct RecipesView: View {
    
//    @State var buttonTapped: Bool = false
    //    var recipes: [Recipes] = []
    
    var body: some View {
        
        //DESIGN ---------------------------------
        VStack {
            RoundedRectangle(cornerRadius: 5.0)
                .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                .frame(width: 419, height: 120)
                .overlay(Text("Recipes")
                    .font(.custom("Hiragino Sans W3", size: 34))
                    .foregroundColor(.white)
                    , alignment:
                    .center)
            
            HStack {
                Button(action: { print("All") })  {
                    Text("All Recipes")
                        .font(.custom("Hiragino Sans W3", size: 22))
                        .foregroundColor(.gray)
                        .frame(width: 190, height: 80)
                }.buttonStyle(PrimaryButtonStyle())
                .overlay(
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)
                )

                Button(action: { print("Saved") }) {
                    Text("Saved Recipes")
                        .font(.custom("Hiragino Sans W3", size: 22))
                        .foregroundColor(.gray)
                        .frame(width: 190, height: 80)
                }.buttonStyle(PrimaryButtonStyle())
                .overlay(
                    RoundedRectangle(cornerRadius: 15)
                        .stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)
                )
            }
            
            NavigationView {
                List(1...5, id: \.self) { index in
                    NavigationLink(
                        destination: Text("Food Details"),
                        label: {
                            Text("Food Item #\(index)")
                                .font(.custom("Hiragino Sans W3", size: 22))
                                .foregroundColor(.gray)
                        }).navigationBarTitle("")
                        .navigationBarHidden(true)
                }
            }
            .navigationBarTitle("")
            .navigationBarHidden(true)
            
            Button(action: { print("Generate Recipes") }) {
                Text("GENERATE NEW RECIPES")
                    .frame(width: 320, height: 40)
                    .padding()
                    .font(.custom("Hiragino Sans W3", size: 18))
                    .foregroundColor(.gray)
                    .multilineTextAlignment(.center)
            }.buttonStyle(PrimaryButtonStyle())
            .overlay(
                RoundedRectangle(cornerRadius: 15)
                    .stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)
            )
            
            
            Spacer()
        }
    }
    
    struct ContentView_Previews: PreviewProvider {
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
