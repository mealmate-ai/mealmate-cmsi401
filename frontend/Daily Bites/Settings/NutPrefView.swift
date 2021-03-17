import SwiftUI
import UIKit

let allCuisineChoices: [CuisineChoice] = [CuisineChoice(name: "African"), CuisineChoice(name: "American"), CuisineChoice(name: "British"), CuisineChoice(name: "Cajun"), CuisineChoice(name: "Caribbean"), CuisineChoice(name: "Chinese"), CuisineChoice(name: "Eastern European"), CuisineChoice(name: "European"), CuisineChoice(name: "French"), CuisineChoice(name: "German"), CuisineChoice(name: "Greek"), CuisineChoice(name: "Indian"), CuisineChoice(name: "Irish"), CuisineChoice(name: "Italian"), CuisineChoice(name: "Japanese"), CuisineChoice(name: "Jewish"), CuisineChoice(name: "Korean"), CuisineChoice(name: "Latin American"), CuisineChoice(name: "Mediterranean"), CuisineChoice(name: "Mexican"), CuisineChoice(name: "Middle Eastern"), CuisineChoice(name: "Nordic"), CuisineChoice(name: "Southern"), CuisineChoice(name: "Spanish"), CuisineChoice(name: "Thai"), CuisineChoice(name: "Vietnamese")]

let allDietChoices: [DietChoice] = [DietChoice(name: "Gluten Free"), DietChoice(name: "Ketogenic"), DietChoice(name: "Vegetarian"), DietChoice(name: "Lacto-Vegetarian"), DietChoice(name: "Ovo-Vegetarian"), DietChoice(name: "Vegan"), DietChoice(name: "Pescatarian"), DietChoice(name: "Paleo"), DietChoice(name: "Primal"), DietChoice(name: "Whole30")]

let allDietaryResChoices: [DietaryResChoice] = [DietaryResChoice(name: "Dairy"), DietaryResChoice(name: "Egg"), DietaryResChoice(name: "Gluten"), DietaryResChoice(name: "Grain"), DietaryResChoice(name: "Seafood"), DietaryResChoice(name: "Sesame"), DietaryResChoice(name: "Shellfish"), DietaryResChoice(name: "Soy"), DietaryResChoice(name: "Sulfite"), DietaryResChoice(name: "Tree Nut"), DietaryResChoice(name: "Wheat")]

let allNutGoalChoices: [NutGoalChoice] = [NutGoalChoice(name: "Lose Weight"), NutGoalChoice(name: "Gain Weight"), NutGoalChoice(name: "Same Weight")]

struct NutPrefView: View {
    
    @State private var restrictions = ""
    
    @State private var cuisines = 1
    @State private var diets = 1
    @State private var dietsRes = 1
    
    @State var cuisine = Cuisine(name: "", cuisineItems: [allCuisineChoices[1]])
    
    @State var diet = Diet(name: "", dietItems: [allDietChoices[1]])
    
    @State var dietRes = Dietary(name: "", dietaryResItems: [allDietaryResChoices[1]])
    
    @State var nutGoals = Goals(name: "", nutGoalItems: [allNutGoalChoices[1]])
    
    var body: some View {
        
        NavigationView{
            VStack {
                RoundedRectangle(cornerRadius: 5.0)
                    .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                    .frame(width: 414, height: 120)
                    .overlay(Text("Nutritional Preferences")
                        .font(.custom("Hiragino Sans W3", size: 34))
                        .foregroundColor(.white)
//                        .offset(y: 17)
                        , alignment:
                        .center)
                
                Form {
                    Section {
                        MultiSelector(
                            label: Text("CUISINE CHOICES")
                                .font(.custom("Hiragino Sans W3", size: 14))
                                .foregroundColor(.gray),
                            options: allCuisineChoices,
                            optionToString: { $0.name },
                            selected: $cuisine.cuisineItems
                        )
                        
                    }
                }
                
                Form {
                    Section {
                        MultiSelector(
                            label: Text("DIETS")
                                .font(.custom("Hiragino Sans W3", size: 14))
                                .foregroundColor(.gray),
                            options: allDietChoices,
                            optionToString: { $0.name },
                            selected: $diet.dietItems
                        )
                    }
                }
                
                Form {
                    Section {
                        MultiSelector(
                            label: Text("DIETARY RESTRICTIONS")
                                .font(.custom("Hiragino Sans W3", size: 14))
                                .foregroundColor(.gray),
                            options: allDietaryResChoices,
                            optionToString: { $0.name },
                            selected: $dietRes.dietaryResItems
                        )
                    }
                }
                
                Form {
                    Section {
                        MultiSelector(
                            label: Text("NUTRITION GOAL")
                                .font(.custom("Hiragino Sans W3", size: 14))
                                .foregroundColor(.gray),
                            options: allNutGoalChoices,
                            optionToString: { $0.name },
                            selected: $nutGoals.nutGoalItems
                        )
                    }
                }
                
                    TextField("Other Dietary Restrictions", text: $restrictions, onEditingChanged: { (changed) in
                        print("Restrictions onEditingChanged - \(changed)")
                    })
                    {
                        print("Restrictions onCommit")
                    }
                    .padding()
                    .frame(width: 365, height: 35)
                    .overlay(RoundedRectangle(cornerRadius: 10).stroke(Color.gray, lineWidth: 1))
                    
                    Text("\(restrictions)")
                    
                
                Button(action: {
                    print("Update")
                }, label: {
                    NavigationLink(destination: SettingsView()) {
                        RoundedRectangle(cornerRadius: 20)
                            .fill(Color(red: 4 / 255, green: 146 / 255, blue: 194 / 255))
                            .frame(width: 320, height: 45)
                            //                        .padding()
                            .overlay(
                                Text("Update Preferences")
                                    .font(.custom("Hiragino Sans W3", size: 18))
                                    .foregroundColor(.white)
                    )}
                    .navigationBarHidden(true)
                    .navigationBarTitle("")
                })
                
                Spacer()
                Spacer()
                //                .navigationBarHidden(true)
                //                .navigationBarTitle("")
            }
        }.navigationBarHidden(true)
        .navigationBarTitle("")
    }
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            NutPrefView()
                .background(Color(.systemBackground))
                .edgesIgnoringSafeArea(.top)
        }
    }
}


