
import SwiftUI
import UIKit

let allCuisineChoices: [CuisineChoice] = [CuisineChoice(name: "African"), CuisineChoice(name: "American"), CuisineChoice(name: "British"), CuisineChoice(name: "Cajun"), CuisineChoice(name: "Caribbean"), CuisineChoice(name: "Chinese"), CuisineChoice(name: "Eastern European"), CuisineChoice(name: "European"), CuisineChoice(name: "French"), CuisineChoice(name: "German"), CuisineChoice(name: "Greek"), CuisineChoice(name: "Indian"), CuisineChoice(name: "Irish"), CuisineChoice(name: "Italian"), CuisineChoice(name: "Japanese"), CuisineChoice(name: "Jewish"), CuisineChoice(name: "Korean"), CuisineChoice(name: "Latin American"), CuisineChoice(name: "Mediterranean"), CuisineChoice(name: "Mexican"), CuisineChoice(name: "Middle Eastern"), CuisineChoice(name: "Nordic"), CuisineChoice(name: "Southern"), CuisineChoice(name: "Spanish"), CuisineChoice(name: "Thai"), CuisineChoice(name: "Vietnamese")]

let allDietChoices: [DietChoice] = [DietChoice(name: "Gluten Free"), DietChoice(name: "Ketogenic"), DietChoice(name: "Vegetarian"), DietChoice(name: "Lacto-Vegetarian"), DietChoice(name: "Ovo-Vegetarian"), DietChoice(name: "Vegan"), DietChoice(name: "Pescatarian"), DietChoice(name: "Paleo"), DietChoice(name: "Primal"), DietChoice(name: "Whole30"), DietChoice(name: "None")]

let allDietaryResChoices: [DietaryResChoice] = [DietaryResChoice(name: "Dairy"), DietaryResChoice(name: "Egg"), DietaryResChoice(name: "Gluten"), DietaryResChoice(name: "Grain"), DietaryResChoice(name: "Seafood"), DietaryResChoice(name: "Sesame"), DietaryResChoice(name: "Shellfish"), DietaryResChoice(name: "Soy"), DietaryResChoice(name: "Sulfite"), DietaryResChoice(name: "Tree Nut"), DietaryResChoice(name: "Wheat"), DietaryResChoice(name: "None")]

struct SettingsView: View {
    
    @State var name: String = ""
    @State var restrictions: String = ""
    
    @State private var cuisines = 1
    @State private var diets = 1
    @State private var dietsRes = 1
    
    @State var cuisine = Cuisine(name: "", cuisineItems: [allCuisineChoices[1]])
    
    @State var diet = Diet(name: "", dietItems: [allDietChoices[1]])
    
    @State var dietRes = Dietary(name: "", dietaryResItems: [allDietaryResChoices[1]])
    
    @State private var selectedGoals = 0
    var goals = ["Lose Weight", "Gain Weight", "Same Weight"]
    
    var body: some View {
        
        NavigationView{
            VStack {
                RoundedRectangle(cornerRadius: 5.0)
                    .fill(Color(red: 222 / 255, green: 193 / 255, blue: 255 / 255))
                    .frame(width: 414, height: 115)
                    .overlay(Text("Settings")
                        .font(.custom("Hiragino Sans W3", size: 34))
                        .foregroundColor(.gray)
                        .offset(y: 17)
                        , alignment:
                        .center)
                
                VStack(alignment: .leading) {
                    Text("NAME")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 14))
                        .foregroundColor(.gray)
                        .padding(.bottom, 5)
                    TextField("Enter your name", text: $name, onEditingChanged: { (changed) in
                        print("Name onEditingChanged - \(changed)")
                    })
                    {
                        print("Name onCommit")
                    }
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    Text("\(name)")
                    
                }.padding()
                
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
                
                Form {
                    Section(header: Text("Diets")) {
                        MultiSelector(
                            label: Text("Diets"),
                            options: allDietChoices,
                            optionToString: { $0.name },
                            selected: $diet.dietItems
                        )
                    }
                }
                
                Form {
                    Section(header: Text("Dietary Restrictions")) {
                        MultiSelector(
                            label: Text("Dietary Restrictions"),
                            options: allDietaryResChoices,
                            optionToString: { $0.name },
                            selected: $dietRes.dietaryResItems
                        )
                    }
                }
                
                VStack(alignment: .leading) {
                    Text("OTHER RESTRICTIONS")
                        .fontWeight(.regular)
                        .font(.custom("Hiragino Sans W3", size: 14))
                        .foregroundColor(.gray)
                        .padding(.bottom, 5)
                    TextField("Enter your other dietary restrictions", text: $restrictions, onEditingChanged: { (changed) in
                        print("Restrictions onEditingChanged - \(changed)")
                    })
                    {
                        print("Restrictions onCommit")
                    }
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                    
                    Text("\(restrictions)")
                    
                }.padding()
                
                Picker(selection: $selectedGoals, label: Text("Nutrition Goals")) {
                    ForEach(0 ..< goals.count) {
                        Text(self.goals[$0])
                    }
                }
                
//                Text("You selected: \(goals[selectedGoals])")
        
        Spacer()
    }
}
}
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        SettingsView()
    }
}

