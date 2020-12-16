import SwiftUI
import UIKit

struct LoginView: View {
    
    var body: some View {
        NavigationView{
            ZStack{
                VStack {
                    
                    Text("Welcome to Daily Bites!")
                        .fontWeight(.bold)
                        .font(.custom("Hiragino Sans W3", size: 31))
                        .foregroundColor(.gray)
                    
                    Image("Daily_Bites_Logo")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .padding(10)
                    
                    Button(action: {print("?")}) {
                        Text("Log In")
                            .font(.custom("Hiragino Sans W3", size: 25))
                            .foregroundColor(.gray)
                            .padding(18)
                    }
                    
                    Button(action: {print("?")}) {
                        Text("Register")
                            .font(.custom("Hiragino Sans W3", size: 25))
                            .foregroundColor(.gray)
                            .padding(18)
                    }
                }
            }
        }
    }
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            LoginView()
        }
    }
}

