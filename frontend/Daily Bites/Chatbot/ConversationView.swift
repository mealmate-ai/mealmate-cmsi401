//
//  ConversationView.swift
//  Daily Bites
//
//  Created by Maya Dahlke on 4/12/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//

import SwiftUI

struct ConversationView: View {
    var body: some View {
        ScrollView(.vertical, showsIndicators: false) {
            VStack {
                ForEach(AllMessages) { chat in
                    ChatCell(data: chat)
                }
            }
        }.padding(.horizontal, 15)
    }
}

struct ConversationView_Previews: PreviewProvider {
    static var previews: some View {
        ConversationView()
    }
}
