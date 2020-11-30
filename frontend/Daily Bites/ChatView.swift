
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
                    .fill(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255))
                    .frame(width: 419, height: 115)
                    .overlay(Text("Chat")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 34))
                        .foregroundColor(.gray)
                        .offset(y: 17)
                        , alignment:
                        .center)
                
                HStack (alignment: .center, spacing: 0, content: {
                    Text("#/# CAL")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 18))
                        .foregroundColor(.gray)
                        .frame(width: 100, height: 30, alignment: .trailing)
                    Spacer()
                })
                
                Rectangle()
                    .fill(Color.gray)
                    .frame(width: 420, height: 2)
                
                Spacer()
                
                ScrollView {
                    /*@START_MENU_TOKEN@*//*@PLACEHOLDER=Content@*/Text("Content")/*@END_MENU_TOKEN@*/
                }
                
                Spacer()
                
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
                        .fill(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255))
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
                                .foregroundColor(.gray)
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
        }
    }
}
