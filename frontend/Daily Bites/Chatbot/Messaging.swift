//
//  Messaging.swift
//  Daily Bites
//
//  Created by Maya Dahlke on 4/12/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//

import Foundation
import SwiftUI

struct Messaging: Identifiable, Equatable {
    var id = UUID()
    var idx: Int
    var message: String
    var myMessage: Bool
}

var AllMessages = [
    Messaging(idx: 0, message: "hello there!!", myMessage: false),
    Messaging(idx: 1, message: "hello there!!", myMessage: true),
    Messaging(idx: 2, message: "hello there!!", myMessage: true),
]
