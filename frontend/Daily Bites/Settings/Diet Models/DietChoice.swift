import Foundation

struct DietChoice: Hashable, Identifiable {
    var id: String { name }
    var name: String
}
