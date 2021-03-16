
import SwiftUI
import UIKit

struct ChatView: View {
        
    @State var message: String = ""
    
    //    @Binding var text: String
    //    @State private var isEditing = false
    
    var body: some View {
        
        //DESIGN ---------------------------------
        ZStack{
            VStack {
                
                RoundedRectangle(cornerRadius: 5.0)
                    .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                    .frame(width: 419, height: 120)
                    .overlay(Text("Chat")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 34))
                        .foregroundColor(.white)
                        , alignment:
                        .center)
                
                Spacer()
                
                ScrollView {
                    /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Content@*/Text("Content")/*@END_MENU_TOKEN@*/
                }
                
                Spacer()
                
                VStack(alignment: .leading){
                    HStack(alignment: .bottom){
                        Spacer()
                        Button(action: {
                            print("?")
                        }) {
                            Image(systemName: "mic")
                                .font(.largeTitle)
                                .foregroundColor(.gray)
                                .frame(width: 34, height: 30, alignment: .leading)
                        }
                        Button(action: {
                            print("?")
                        }) {
                            Image(systemName: "barcode")
                                .font(.largeTitle)
                                .foregroundColor(.gray)
                                .frame(width: 40, height: 30, alignment: .leading)
                        }
                        Button(action: {
                            print("?")
                        }) {
                            Image(systemName: "camera")
                                .font(.largeTitle)
                                .foregroundColor(.gray)
                                .frame(width: 50, height: 30, alignment: .leading)
                        }
                    }
                }
                
                
                HStack (alignment: .center, spacing: 0, content: {
                    RoundedRectangle(cornerRadius: 5.0)
                        .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                        .frame(width: 419, height: 55)
                    .overlay(TextField("Enter food items", text: $message)
                        .background(Color.white)
                        .border(Color(UIColor.separator))
                        .frame(width: 335, height: 30, alignment: .leading)
                        .multilineTextAlignment(.leading)
                        .padding(.trailing, 40) .textFieldStyle(RoundedBorderTextFieldStyle())
                    )
                        
//                        Text("\(message)")
                        .overlay(Button(action: {
                            print("?")
                        }) {
                            Image(systemName: "arrow.up.square")
                                .font(.largeTitle)
                                .foregroundColor(.white)
                                .padding(.leading, 350.0)
                        }
                    )
                })
            }
            Spacer()
        }
    }
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            ChatView()
                .background(Color(.systemBackground))
                .edgesIgnoringSafeArea(.top)
        }
    }
}
