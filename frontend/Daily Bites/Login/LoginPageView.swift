import SwiftUI
import UIKit

struct LoginPageView: View {
    
    @State var email: String = ""
    @State private var password: String = ""
    @State private var secured: Bool = true
    @State private var action: Int? = 0
    
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
                
                TextField("Email", text: $email, onEditingChanged: { (changed) in
                    print("Email onEditingChanged - \(changed)")
                })
                {
                    print("Email onCommit")
                }
                .frame(width: 340, height: 4)
                .padding()
                .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                
                Text("\(email)")
                
                
                HStack {
                    
                    if (secured) {
                        SecureField("Password", text: $password)
                            .padding()
                            .frame(width: 340, height: 36)
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                    } else {
                        TextField("Password", text: $password)
                            .frame(width: 300, height: 36)
                            .padding()
                            .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))                        }
                    //                        ({
                    //                            print("Password onCommit")
                    //                        })
                    
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
                    print("Login")
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
                })
                
                Spacer()
                Spacer()
                Spacer()
                
            }
        }
    }
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            LoginPageView()
                .background(Color(.systemBackground))
        }
    }
    
}
