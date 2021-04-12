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
    var id: Int
    var message: String
    var myMessage: Bool
}

var AllMessages = [
    Messaging(id:0, message: "hello there!!", myMessage: false),
    Messaging(id:1, message: "hello there!!", myMessage: true),
    Messaging(id:2, message: "hello there!!", myMessage: false),
]
