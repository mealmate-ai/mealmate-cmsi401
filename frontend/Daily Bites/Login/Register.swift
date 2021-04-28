//
//  Register.swift
//  Daily Bites
//
//  Created by Lexi Weingardt on 4/19/21.
//  Copyright © 2021 Lexi Weingardt. All rights reserved.
//  http://ec2-3-16-149-133.us-east-2.compute.amazonaws.com:8080/get-recipes/


import SwiftUI

struct UserInfo: Codable, Identifiable {
    var id = UUID()
    var name: String = ""
    var email: String = ""
    private var password: String = ""
}
