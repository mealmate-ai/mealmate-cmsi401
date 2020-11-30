
import SwiftUI
import UIKit

struct SettingsView: View {
    
    @State var name: String = ""
    //    @State var expand = false
    @State private var cuisines = 1
    @State private var diets = 1
    
    var body: some View {
        
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
                    .font(.custom("Hiragino Sans W3", size: 18))
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
            
            VStack(alignment: .leading){
                Picker(selection: $cuisines, label: Text("CUISINES")
                    .font(.custom("Hiragino Sans W3", size: 16))
                    .foregroundColor(.gray))
                {
                    Text("African").tag(1)
                    Text("American").tag(2)
                    Text("British").tag(3)
                    Text("Cajun").tag(4)
                    Text("Caribbean").tag(5)
                    Text("Chinese").tag(6)
                    Text("Eastern European").tag(7)
                    Text("European").tag(8)
                    Text("French").tag(9)
                    Text("German").tag(10)
                }
            }
            
            VStack(alignment: .leading){
                Picker(selection: $diets, label: Text("DIETS")
                    .font(.custom("Hiragino Sans W3", size: 16))
                    .foregroundColor(.gray))
                {
                    Text("Gluten Free").tag(1)
                    Text("Ketogenic").tag(2)
                    Text("Vegetarian").tag(3)
                    Text("Lacto-Vegetarian").tag(4)
                    Text("Ovo-Vegetarian").tag(5)
                    Text("Vegan").tag(6)
                    Text("Pescatarian").tag(7)
                    Text("Paleo").tag(8)
                    Text("Primal").tag(9)
                    Text("Whole30").tag(10)
                }
            }
            
            //            VStack{
            //                HStack{
            //                    Text("CUISINES")
            //                        .foregroundColor(.gray)
            //                        .font(.custom("Hiragino Sans W3", size: 16))
            //                        .padding(.bottom, 5)
            //                    Image(systemName: expand ? "chevron.up" : "chevron.down")
            //                        .resizable()
            //                        .frame(width: 10, height: 10)
            //                        .foregroundColor(.gray)
            //                        .onTapGesture(count: 1) {
            //                            self.expand.toggle()
            //                        }
            //                }
            //                if expand{
            //                    Button(action: {
            //                        print("1")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("African")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("2")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("American")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("3")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("British")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("4")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Cajun")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("5")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Caribbean")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("6")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Chinese")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("7")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Eastern European")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("8")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("European")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("9")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("French")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("10")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("German")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("11")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Greek")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                }
            //            }
            //
            //            Spacer()
            //
            //            VStack{
            //                HStack{
            //                    Text("DIETS")
            //                        .foregroundColor(.gray)
            //                        .font(.custom("Hiragino Sans W3", size: 16))
            //                        .padding(.bottom, 5)
            //                    Image(systemName: expand ? "chevron.up" : "chevron.down")
            //                        .resizable()
            //                        .frame(width: 10, height: 10)
            //                        .foregroundColor(.gray)
            //                        .onTapGesture(count: 1) {
            //                            self.expand.toggle()
            //                    }
            //                }
            //                if expand{
            //                    Button(action: {
            //                        print("1")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Gluten Free")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("2")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Ketogenic")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("3")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Vegetarian")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("4")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Lacto-Vegetarian")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("5")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Ovo-Vegetarian")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("6")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Vegan")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("7")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Pescatarian")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("8")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Paleo")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("9")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Primal")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("10")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Whole30")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                    Button(action: {
            //                        print("11")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Greek")
            //                            .padding(5)
            //                    }.foregroundColor(.gray)
            //                }
            //            }
            
            
            //
            //
            //
            //
            //
            //
            //                    Button(action: {
            //                        print("12")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Indian")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("13")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Irish")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("14")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Italian")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("15")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Japanese")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("16")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Jewish")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("17")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Korean")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("18")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Latin American")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("19")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Mediterranean")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("20")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Mexican")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("21")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Middle Eastern")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("22")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Nordic")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("23")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Southern")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("24")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Spanish")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("25")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Thai")
            //                            .padding(10)
            //                    }
            //                    Button(action: {
            //                        print("25")
            //                        self.expand.toggle()
            //                    }) {
            //                        Text("Vietnamese")
            //                            .padding(10)
            //                    }
            //                }
            //                .padding()
            //                    .cornerRadius(15)
            //                    .shadow(color: .gray, radius: 3)
            //                    .animation(.spring())
            //            }
            Spacer()
        }
    }
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            SettingsView()
        }
    }
}

