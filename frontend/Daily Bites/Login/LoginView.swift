import SwiftUI
import UIKit

struct LoginView: View {
    
    var body: some View {
        
        NavigationView{
            ZStack{
                VStack {
                    
                    Image("new_daily_bites_logo")
                        .resizable()
                        .aspectRatio(contentMode: .fit)
                        .padding(40)
                    
                    Spacer()
                    
                    NavigationLink(destination: LoginPageView()) {
                        RoundedRectangle(cornerRadius: 26)
                            .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                            .frame(width: 320, height: 45)
                            .overlay(
                                Text("LOGIN")
                                    .padding()
                                    .font(.custom("Hiragino Sans W3", size: 20))
                                    .foregroundColor(.white)
<<<<<<< HEAD
                            )}.navigationBarTitle("")
                        .navigationBarHidden(true)
=======
                            )}.navigationBarHidden(true).navigationBarTitle("")
                        
>>>>>>> bree-spring
                    
                    NavigationLink(destination: RegisterView()) {
                        RoundedRectangle(cornerRadius: 26)
                            .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                            .frame(width: 320, height: 45)
                            .padding()
                            .overlay(
                                Text("REGISTER")
                                    .font(.custom("Hiragino Sans W3", size: 20))
                                    .foregroundColor(.white)
<<<<<<< HEAD
                            )}
                    Spacer()
                }
            }
        }
=======
                            )}.navigationBarHidden(true)
                        .navigationBarTitle("")
                        
                    Spacer()
                }
            }
        }.navigationBarHidden(true)
        .navigationBarTitle("")
>>>>>>> bree-spring
    }
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            LoginView()
                .background(Color(.systemBackground))
        }
    }
}

