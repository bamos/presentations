// Regenerate the reference glyph on macOS: swift scripts/render-book-emoji.swift
// The PNG is retained as an input, so other platforms do not need Swift.
import AppKit
let size = 256
let bitmap = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: size, pixelsHigh: size,
    bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
    colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: bitmap)
let text = NSAttributedString(string: "📚", attributes: [
    .font: NSFont(name: "Apple Color Emoji", size: 205)!
])
let extent = text.size()
text.draw(at: NSPoint(x: (CGFloat(size)-extent.width)/2,
                     y: (CGFloat(size)-extent.height)/2))
NSGraphicsContext.restoreGraphicsState()
try bitmap.representation(using: .png, properties: [:])!
    .write(to: URL(fileURLWithPath: "assets/book-emoji.png"))
