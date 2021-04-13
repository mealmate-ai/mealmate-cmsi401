//
//  Messaging.swift
//  Daily Bites
//
//  Created by Maya Dahlke on 4/12/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//

import Foundation
import SwiftUI

struct Messaging: Identifiable {
    var id = UUID()
    var message: String
    var myMessage: Bool
}

var AllMessages = [
    Messaging(message: "hello there!!", myMessage: false),
    Messaging(message: "hello there!!", myMessage: true),
    Messaging(message: "hello there!!", myMessage: true),
]
