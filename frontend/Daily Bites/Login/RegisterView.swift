
import SwiftUI
import UIKit


struct RegisterView: View {
    
    @State var name: String = ""
    @State var email: String = ""
    @State private var password: String = ""
    @State private var secured: Bool = true
    
    var body: some View {
        
        NavigationView{
            VStack {
                
                Image("new_daily_bites_logo")
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                    .padding(.vertical, 40)
                    .padding(.horizontal, 80)
                
                Spacer()
                
                TextField("Name", text: $name)
                    .padding()
                    .frame(width: 365, height: 35)
                    .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                    .padding()
                
                TextField("Email", text: $email)
                    .padding()
                    .frame(width: 365, height: 35)
                    .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                
                
                HStack {
                    
                    if (secured) {
                        SecureField("Password", text: $password)
                            .padding()
                            .frame(width: 328, height: 35)
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                            .padding()
                    } else {
                        TextField("Password", text: $password)
                            .padding()
                            .frame(width: 328, height: 35)
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                            .padding()
                    }
                    
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
                
                VStack {
                    NavigationLink(destination: NutPrefView()) {
                        Text("CHOOSE NUTRITIONAL PREFERENCES")
                            .frame(width: 320, height: 40)
                            .padding()
                            .font(.custom("Hiragino Sans W3", size: 18))
                            .foregroundColor(.gray)
                            .multilineTextAlignment(.center)
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255), lineWidth: 1)).padding(20)
                    }
                    .navigationBarTitle("")
                    .navigationBarHidden(true)
                    
                    Button(action: {
                        self.createUser()
                    }, label: {
                        NavigationLink(destination: ContentView()) {
                            RoundedRectangle(cornerRadius: 18)
                                .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                                .frame(width: 320, height: 45)
                                .padding()
                                .overlay(
                                    Text("Create Account")
                                        .font(.custom("Hiragino Sans W3", size: 18))
                                        .foregroundColor(.white)
                                )}.navigationBarHidden(true)
                            .navigationBarTitle("")
                    }).disabled(name.isEmpty || email.isEmpty || password.isEmpty)
                }
                
                Spacer()
                Spacer()
            }
        }.navigationBarHidden(true)
        .navigationBarTitle("")
    }
    
    func createUser(){
        guard let encoded = try? JSONEncoder().encode([name, email, password])
        else{
            print("Failed to encode user")
            return
        }
        
        let url = URL(string: "https://reqres.in/api/cupcakes")!
        var request = URLRequest(url: url)
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpMethod = "POST"
        request.httpBody = encoded
        
        URLSession.shared.dataTask(with: request) { data, response, error in
            guard data != nil else {
                print("No data in response: \(error?.localizedDescription ?? "Unknown error").")
                return
            }

            // handle the result here.
        }.resume()
    }

    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            RegisterView()
                .background(Color(.systemBackground))
        }
    }
}
