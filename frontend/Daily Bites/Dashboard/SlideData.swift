
import Foundation
import SwiftUI

class SlideData: Identifiable, ObservableObject {
    let id: UUID = UUID()
    var data: DataItem!
    var annotation: String! = ""
    var startAngle: Angle! = .degrees(0)
    var endAngle: Angle! = .degrees(0)
    var percentage = ""
}
