

struct EyeImage: View {
    
    private var imageName: String
    init(name: String) {
        self.imageName = name
    }
    
    var body: some View {
        Image(imageName)
            .resizable()
            .foregroundColor(.black)
            .frame(width: 44, height: 44, alignment: .trailing)
    }
}
