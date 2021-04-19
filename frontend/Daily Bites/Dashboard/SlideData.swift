
import Foundation
import SwiftUI

class SlideData: Identifiable, ObservableObject {
    let id: UUID = UUID()
    var data: DataItem!
    var annotation: String! = ""
    var startAngle: Angle! = .degrees(0)
    var endAngle: Angle! = .degrees(0)
    var percentage = ""
    
    var annotationDeltaX: CGFloat! = 0.0
    var annotationDeltaY: CGFloat! = 0.0
//make percentage grams that is an int
    
    init(startAngle: Angle, endAngle: Angle) {
            self.data = DataItem(name: "", value: 0)
            self.startAngle = startAngle
            self.endAngle = endAngle
    }
}
