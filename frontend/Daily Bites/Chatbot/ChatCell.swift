//
//  ChatCell.swift
//  Daily Bites
//
//  Created by Maya Dahlke on 4/12/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//

import SwiftUI

struct ChatCell: View {
    var data: Messaging
    var body: some View {
        HStack {
            if data.myMessage {
                Spacer()
                Text(data.message)
                    .padding()
                    .background(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255)).clipShape(MessageTail(myMessage: data.myMessage)).foregroundColor(.white)
            } else {
                Text(data.message)
                    .padding()
                    .foregroundColor(.primary)
                    .background(Color.secondary.opacity(0.2))
                    .clipShape(MessageTail(myMessage: data.myMessage))
                Spacer()
            }
        }.padding(data.myMessage ? .leading: .trailing, 55).padding(.vertical, 10)
    }
}

struct ChatCell_Previews: PreviewProvider {
    static var previews: some View {
        ChatCell(data: AllMessages[1])
    }
}
