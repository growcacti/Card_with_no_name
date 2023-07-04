# Handle events
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button pressed
            for card_sprite in card_sprites:
                if card_sprite.rect.collidepoint(event.pos):
                    card_sprite.dragging = True
                    card_sprite.offset_x = event.pos[0] - card_sprite.rect.x
                    card_sprite.offset_y = event.pos[1] - card_sprite.rect.y

    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:  # Left mouse button released
            for card_sprite in card_sprites:
                if card_sprite.dragging:
                    card_sprite.dragging = False
                    # Perform additional actions based on the drop position

    elif event.type == pygame.MOUSEMOTION:
        for card_sprite in card_sprites:
            if card_sprite.dragging:
                card_sprite.rect.x = event.pos[0] - card_sprite.offset_x
                card_sprite.rect.y = event.pos[1] - card_sprite.offset_y
