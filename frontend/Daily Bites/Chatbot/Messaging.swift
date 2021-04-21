//
//  Messaging.swift
//  Daily Bites
//
//  Created by Maya Dahlke on 4/12/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//

import Foundation
import SwiftUI

struct Messaging: Codable, Identifiable, Equatable {
    var id = UUID()
    let idx: Int
    let message: String
    let myMessage: Bool
}

struct MessagingRasa: Codable, Identifiable {
    let id: Int
    let title: String
    let body: String
}

class ApiChat {
    func getChatResponse(completion: @escaping ([MessagingRasa]) -> ()) {
       guard let url = URL(string: "https://jsonplaceholder.typicode.com/posts") else {return}
        //http://ec2-3-17-5-22.us-east-2.compute.amazonaws.com:5005/401-chatbot/model/parse
        URLSession.shared.dataTask(with: url) { (data, _, _) in
            print(data!)
            let chatResponse = try! JSONDecoder().decode([MessagingRasa].self, from:data!)
            //let rasaMessage = chatResponse.description
            //print(rasaMessage)
            
            DispatchQueue.main.async {
                completion(chatResponse)
            }
        }
        .resume()
    }
}

//var AllMessages = [
//    Messaging(idx: 0, message: "hello there!!", myMessage: false),
//    Messaging(idx: 1, message: "hello there!!", myMessage: true),
//    Messaging(idx: 2, message: "hello there!!", myMessage: true),
//]
