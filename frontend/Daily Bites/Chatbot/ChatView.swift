import SwiftUI
import UIKit

struct ChatView: View {
        
    @State var message: String = ""
    @State var messages: [Messaging] = AllMessages
    
    //    @Binding var text: String
    //    @State private var isEditing = false
    
    var body: some View {
            
        VStack {
                
                RoundedRectangle(cornerRadius: 5.0)
                    .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                    .edgesIgnoringSafeArea(.top)
                    .frame(width: 425, height: 50)
                    .overlay(Text("Chat")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 34))
                        .foregroundColor(.white)
                                .offset(y: -20)
                        , alignment:
                        .center)
                
                Spacer()
                
                ConversationView(messages: $messages)
                
                Spacer()
                
                VStack(alignment: .leading) {
                    HStack(alignment: .bottom) {
                        Spacer()
                        Button(action: {
                            print("?")
                        }) {
                            Image(systemName: "mic.fill")
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
                            Image(systemName: "camera.fill")
                                .font(.largeTitle)
                                .foregroundColor(.gray)
                                .frame(width: 50, height: 30, alignment: .leading)
                                .padding(.trailing)
                        }
                    }
                }
                
                VStack {
                    HStack(spacing: 20) {
                        ChatTextView(text: $message).frame(numLines: 1)
                            .font(.headline)
                            .padding(.leading)
                            .multilineTextAlignment(.leading)
                        Spacer()
                        Button(action: {
                            let newIndex = messages.count
                            let mess = Messaging(idx:newIndex, message: "\(message)", myMessage: true)
                            messages.append(mess)
                            message = ""
                        }) {
                            Image(systemName: "arrow.up.circle.fill").font(.title).foregroundColor(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                        }
                    }.padding(EdgeInsets(top: 8, leading: 8, bottom: 8, trailing: 8))
                    .foregroundColor(.secondary).background(Color.white).clipShape(Capsule()).shadow(radius: 1).padding()
                }.frame(height:70).background(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ChatView()
    }
}
