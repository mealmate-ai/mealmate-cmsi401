
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
<<<<<<< HEAD
                    
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
                    //                        ({
                    //                            print("Password onCommit")
                    //                        })
                    
=======
                    
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
                    //                        ({
                    //                            print("Password onCommit")
                    //                        })
                    
>>>>>>> bree-spring
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
                        print("New Account")
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
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            RegisterView()
                .background(Color(.systemBackground))
        }
    }
}
