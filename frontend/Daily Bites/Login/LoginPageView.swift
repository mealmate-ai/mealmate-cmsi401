import SwiftUI
import UIKit

struct LoginPageView: View {
    
    @State var email: String = ""
    @State var password: String = ""
    
    var body: some View {
        
        //DESIGN ---------------------------------
        ZStack{
            VStack {
                Rectangle()
                    .fill(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255))
                    .frame(width: 419, height: 115)
                    .overlay(Text("Login")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 34))
                        .foregroundColor(.gray)
                        .offset(y: 17)
                        , alignment:
                        .center)
                    .cornerRadius(5.0)
                
                
                VStack(alignment: .leading) {
                    Text("EMAIL")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 14))
                        .foregroundColor(.gray)
                        .padding(.bottom, 5)
                    TextField("Enter your email", text: $email, onEditingChanged: { (changed) in
                        print("Email onEditingChanged - \(changed)")
                    })
                    {
                        print("Email onCommit")
                    }
                    .padding(5)
                    .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                    
                    Text("\(email)")
                    
                }.padding()
                
                VStack(alignment: .leading) {
                    Text("PASSWORD")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 14))
                        .foregroundColor(.gray)
                        .padding(.bottom, 5)
                    TextField("Enter your password", text: $email, onEditingChanged: { (changed) in
                        print("Password onEditingChanged - \(changed)")
                    })
                    {
                        print("Password onCommit")
                    }
                    .padding(5)
                    .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                    
                    Text("\(password)")
                    
                }.padding()
                
                Button(action: {print("logged in")}) {
                    Text("Login")
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
            LoginPageView()
        }
    }
}
