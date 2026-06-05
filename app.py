# Pseudo-code (gambaran logika)
import pygame

# 1. Setup Gambar
keranjang_rect = pygame.Rect(500, 400, 100, 100) # Area keranjang
kue_rect = pygame.Rect(100, 100, 50, 50)         # Posisi kue di etalase

# 2. Loop Utama Game
running = True
dragging = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if kue_rect.collidepoint(event.pos):
                dragging = True
        
        if event.type == pygame.MOUSEBUTTONUP:
            dragging = False
            # Cek apakah dilepas di atas keranjang
            if kue_rect.colliderect(keranjang_rect):
                print("Kue masuk keranjang!")
                keranjang_belanja.append("Kue Coklat")

    if dragging:
        kue_rect.center = pygame.mouse.get_pos() # Ikuti kursor
