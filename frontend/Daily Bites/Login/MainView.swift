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
                    
                    VStack {
                        NavigationLink(destination: LoginPageView()) {
                            Text("LOGIN")
                                .frame(width: 150, height: 30)
                                .padding()
                                .font(.custom("Hiragino Sans W3", size: 20))
                                .foregroundColor(.gray)
                            .overlay(
                                        RoundedRectangle(cornerRadius: 20)
                                            .stroke(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255), lineWidth: 3)
                            )
                        }
                    }
                    
                    VStack {
                        NavigationLink(destination: RegisterView()) {
                            Text("REGISTER")
                                .frame(width: 150, height: 30)
                                .padding()
                                .font(.custom("Hiragino Sans W3", size: 20))
                                .foregroundColor(.gray)
                            .overlay(
                                        RoundedRectangle(cornerRadius: 20)
                                            .stroke(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255), lineWidth: 3)
                            )
                        }
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

