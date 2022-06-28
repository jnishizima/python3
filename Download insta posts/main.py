import instaloader

# Carrega a lib e faz login com a conta desejada #
L = instaloader.Instaloader()
L.login('** Usuario **', '** Senha **')

# Carrega todos os posts do perfil escolhido #
posts = instaloader.Profile.from_username(L.context, "** perfil **").get_posts()

# Percorre os posts e baixa apenas os que estão dentro do período desejado #
for post in posts:
    print(post.date)
    L.download_post(post, "downloads")