//
//  ConversationView.swift
//  Daily Bites
//
//  Created by Maya Dahlke on 4/12/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//

import SwiftUI

struct ConversationView: View {
    
    @State var m: String = ""
    @Binding var messages: [Messaging]
    
    var body: some View {
        ScrollView(.vertical, showsIndicators: false) {
            if #available(iOS 14.0, *) {
                ScrollViewReader { scrollView in
                    VStack {
                        ForEach(messages) { message in
                            ChatCell(data: message)
                        }
                    }.onChange(of: messages, perform: { value in
                        DispatchQueue.main.async {
                            scrollView.scrollTo(messages[messages.endIndex-1].id, anchor: .bottom)
                        }
                    })
                }
            } else {
                // Fallback on earlier versions
            }
        }.padding(.horizontal, 25)
    }
    
//    func addItem(mess: String) {
//        m = mess
//        let newIndex = messages.count
//        let message = Messaging(idx:newIndex, message: mess, myMessage: true)
//        messages.append(message)
//        print(messages)
//    }
 
}

