use image::io::Reader as ImageReader;
use glob::glob;

fn convert_jpeg_to_png(jpeg_path: &str, png_path: &str) -> Result<(), image::ImageError> {
    let img = ImageReader::open(jpeg_path)?.decode()?;
    img.save(png_path)?;
    Ok(())
}

fn convert_all_jpegs_in_directory(directory: &str) -> Result<(), image::ImageError> {
    let pattern = format!("{}/*.jpeg", directory);

    for entry in glob(&pattern).expect("Failed to read glob pattern") {
        match entry {
            Ok(path) => {
                let jpeg_path = path.display().to_string();
                let png_path = jpeg_path.replace(".jpeg", ".png");

                match convert_jpeg_to_png(&jpeg_path, &png_path) {
                    Ok(_) => println!("Converted: {} to {}", jpeg_path, png_path),
                    Err(e) => println!("Failed to convert {}: {}", jpeg_path, e),
                }
            },
            Err(e) => println!("{:?}", e),
        }
    }

    Ok(())
}

fn main() {
    if let Err(e) = convert_all_jpegs_in_directory("data") {
        println!("Error processing images: {}", e);
    }
}
