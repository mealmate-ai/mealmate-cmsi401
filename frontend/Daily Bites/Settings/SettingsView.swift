
import SwiftUI
import UIKit


struct SettingsView: View {
    
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
                    Text("CHANGE NUTRITIONAL PREFERENCES")
                        .frame(width: 343, height: 40)
                        .padding()
                        .font(.custom("Hiragino Sans W3", size: 18))
                        .foregroundColor(.gray)
                        .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1)).padding(20)
                    }
                }
                
                Button(action: {print("saved")}) {
                    Text("Save")
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
            SettingsView()
        }
    }
}
