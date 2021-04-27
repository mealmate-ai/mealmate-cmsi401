
import SwiftUI
import UIKit


struct SettingsView: View {
    
    //these should be filled based on the user
    @State var name: String = ""
    @State var email: String = ""
    @State var password: String = ""
    
    
    var body: some View {
        
        NavigationView{
            VStack {
                RoundedRectangle(cornerRadius: 5.0)
                    .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                    .frame(width: 419, height: 120)
                    .overlay(Text("Settings")
                        .font(.custom("Hiragino Sans W3", size: 34))
                        .foregroundColor(.white)
                             .offset(y: 20),
                             alignment:
                        .center)
                
                VStack(alignment: .leading) {
                    Text("NAME")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 14))
                        .foregroundColor(.gray)
                        .padding(.bottom, 5)
                    TextField("Enter your name", text: $name)
                        .padding(5)
                        .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                    
                }.padding()
                
                VStack(alignment: .leading) {
                    Text("EMAIL")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 14))
                        .foregroundColor(.gray)
                        .padding(.bottom, 5)
                    TextField("Enter your email", text: $email)
                        .padding(5)
                        .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                    
                }.padding()
                
                VStack(alignment: .leading) {
                    Text("PASSWORD")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 14))
                        .foregroundColor(.gray)
                        .padding(.bottom, 5)
                    TextField("Enter your password", text: $password)
                        .padding(5)
                        .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                    
                }.padding()
                
                VStack {
                    NavigationLink(destination: NutPrefView()) {
                        Text("CHANGE NUTRITIONAL PREFERENCES")
                            .frame(width: 343, height: 40)
                            .padding()
                            .font(.custom("Hiragino Sans W3", size: 18))
                            .foregroundColor(.gray)
                            .multilineTextAlignment(.center)
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)).padding(20)
                    }
                }
                
                Button(action: {
                    print("updated user info")
                }) {
                    RoundedRectangle(cornerRadius: 26)
                        .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                        .frame(width: 320, height: 45)
                        .overlay(
                            Text("Save")
                                .font(.custom("Hiragino Sans W3", size: 18))
                                .foregroundColor(.white)
                    )}
                
                Button(action: {
                    print("Log Out")
                }, label: {
                    NavigationLink(destination: LoginView()) {
                        RoundedRectangle(cornerRadius: 26)
                            .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                            .frame(width: 320, height: 45)
                            .padding(.horizontal, 50)
                            .overlay(
                                Text("Logout")
                                    .font(.custom("Hiragino Sans W3", size: 18))
                                    .foregroundColor(.white)
                        )}.navigationBarHidden(true)
                        .navigationBarTitle("")
                    
                    Spacer()
                })
            }
        }.navigationBarTitle("")
        .navigationBarHidden(true)
    }
    
//    func updateUser(){
//        guard let encoded = try? JSONEncoder().encode([name, email, password])
//        else{
//            print("Failed to encode update for user")
//            return
//        }
//
//        let url = URL(string: "https://reqres.in/api/cupcakes")!
//        var request = URLRequest(url: url)
//        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
//        request.httpMethod = "PATCH"
//        request.httpBody = encoded
//
//        URLSession.shared.dataTask(with: request) { data, response, error in
//            guard data != nil else {
//                print("No data in response: \(error?.localizedDescription ?? "Unknown error").")
//                return
//            }
//
//            // handle the result here.
//        }.resume()
//    }
    
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            SettingsView()
                .background(Color(.systemBackground))
                .edgesIgnoringSafeArea(.top)
        }
    }
}
