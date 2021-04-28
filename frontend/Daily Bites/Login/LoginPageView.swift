import SwiftUI
import UIKit

struct LoginPageView: View {
    
    @State var email: String = ""
    @State private var password: String = ""
    @State private var secured: Bool = true
    @State private var action: Int? = 0
    
    @State private var userToken: String = ""
    
    var body: some View {
        
        //DESIGN ---------------------------------
        NavigationView{
            VStack {
                
                Image("new_daily_bites_logo")
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .padding(.vertical, 40)
                    .padding(.horizontal, 80)
                
                Spacer()

                TextField("Email", text: $email)
                    .frame(width: 340, height: 4)
                    .padding()
                    .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                
                HStack {
                    
                    if (secured) {
                        SecureField("Password", text: $password)
                            .padding()
                            .frame(width: 340, height: 36)
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                    } else {
                        TextField("Password", text: $password)
                            .frame(width: 308, height: 4)
                            .padding()
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))                        }
                    
                    Button(action: {
                        self.secured.toggle()
                    }) {
                        if secured {
                            Image(systemName: "eye.slash.fill")
                        } else {
                            Image(systemName: "eye.fill")
                        }
                    }
                }
                
                Button(action: {
                    self.checkUser()
                }, label: {
                    NavigationLink(destination: ContentView()) {
                        RoundedRectangle(cornerRadius: 18)
                            .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                            .frame(width: 320, height: 45)
                            .padding()
                            .overlay(
                                Text("Login")
                                    .font(.custom("Hiragino Sans W3", size: 18))
                                    .foregroundColor(.white)
                            )}.navigationBarHidden(true)
                        .navigationBarTitle("")
                }).disabled(email.isEmpty || password.isEmpty)
                
                Spacer()
                Spacer()
                Spacer()
                
            }
        }.navigationBarHidden(true)
        .navigationBarTitle("")
        
    }
    
    struct loginResponse: Codable {
        var token: String
    }
    
    func checkUser(){
        guard let encoded = try? JSONEncoder().encode([email, password])
        else{
            print("Failed to encode user")
            return
        }
        
        let url = URL(string: "http://192.168.1.18:8080/login")!
        var request = URLRequest(url: url)
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpMethod = "POST"
        request.httpBody = encoded
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            guard data != nil else {
                print("No data in response: \(error?.localizedDescription ?? "Unknown error").")
                return
            }
            
            if let decodedResponse = try? JSONDecoder().decode(loginResponse.self, from: data!) {
                self.userToken = decodedResponse.token
            } else {
                print("Invalid response from server")
            }
            
        }.resume()
    }
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            LoginPageView()
                .background(Color(.systemBackground))
        }
    }
    
}
