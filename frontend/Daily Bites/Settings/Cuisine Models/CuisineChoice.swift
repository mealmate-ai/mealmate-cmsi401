import Foundation

struct CuisineChoice: Hashable, Identifiable {
    var id: String { name }
    var name: String
}
