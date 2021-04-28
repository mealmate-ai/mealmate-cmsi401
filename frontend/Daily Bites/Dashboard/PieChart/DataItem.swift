
import Foundation
import SwiftUI

extension CGFloat {
    static func random() -> CGFloat {
        return CGFloat(arc4random()) / CGFloat(UInt32.max)
    }
}

extension Color {
    static func random() -> Color {
        return Color(
            red:   .random(in: 0...0.68),
            green: .random(in: 0.56...0.85),
            blue:  .random(in: 0.90...1))
    }
}

class DataItem {
    var name: String! = ""
    var value: Double = 0.0
    var color: Color! = Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255)
    
    init(name: String, value: Double, color: Color? = nil) {
        self.name = name
        self.value = value
        if let color = color {
            self.color = color
        } else {
            self.color = .random()
        }
    }
}

struct DataItem_Previews: PreviewProvider {
    static var previews: some View {
        /*@START_MENU_TOKEN@*/Text("Hello, World!")/*@END_MENU_TOKEN@*/
    }
}

