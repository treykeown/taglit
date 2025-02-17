from taglit import taglit, html

def is_logged_in() -> bool:
    return False

animal_images = ["cat.png", "dog.png", "cow.png"]
status_image = "logged-in.png" if is_logged_in() else "logged-out.png"

@taglit(html, target='f')
def demo():
    return f'''
        <div>
            <img src={status_image}>
            <ul>
                {(f'<li><img src={image_file}></li>' for image_file in animal_images)}
            </ul>
        </div>
    '''

print(demo())
