
import SwiftUI
import UIKit


struct RegisterView: View {

    @State var name: String = ""
    @State var email: String = ""
    @State var password: String = ""



    var body: some View {

        NavigationView{
            VStack {
                RoundedRectangle(cornerRadius: 5.0)
                    .fill(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255))
                    .frame(width: 414, height: 115)
                    .overlay(Text("Settings")
                        .font(.custom("Hiragino Sans W3", size: 34))
                        .foregroundColor(.gray)
                        .offset(y: 17)
                        , alignment:
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
                    Text("CHOOSE NUTRITIONAL PREFERENCES")
                        .frame(width: 400, height: 100)
                        .padding()
                        .font(.custom("Hiragino Sans W3", size: 18))
                        .foregroundColor(.gray)
                    }
                }
                
                Button(action: {print("account made")}) {
                    Text("Create Account")
                        .font(.custom("Hiragino Sans W3", size: 18))
                        .foregroundColor(.gray)
                        .padding()
                        .overlay(
                            RoundedRectangle(cornerRadius: 20)
                                .stroke(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255), lineWidth: 3)
                )}

                
                Spacer()
            }
        }
    }
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            RegisterView()
        }
    }
}
