
import SwiftUI
import UIKit

let allCuisineChoices: [CuisineChoice] = [CuisineChoice(name: "Learn Japanese"), CuisineChoice(name: "Learn SwiftUI"), CuisineChoice(name: "Learn Serverless with Swift")]

struct CuisineEditView: View {
    @State var cuisine = Cuisine(name: "", cuisineItems: [allCuisineChoices[1]])

    var body: some View {
        Form {
            Section(header: Text("Cuisines")) {
                MultiSelector(
                    label: Text("Cuisine Choices"),
                    options: allCuisineChoices,
                    optionToString: { $0.name },
                    selected: $cuisine.cuisineItems
                )
            }
        }
    }
}

struct CuisineEditView_Previews: PreviewProvider {
    static var previews: some View {
        NavigationView {
            CuisineEditView()
        }
    }
}
