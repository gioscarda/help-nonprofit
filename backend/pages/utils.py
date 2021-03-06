import os


class RoutingUtils:

    def __init__(self, path):
        self._path = path

    def get_nuxt_routes(self, nested_path=None):
        from projects.models import Project
        from shop.models import Product
        path = nested_path if nested_path else self._path
        routes = []
        for p in os.listdir(path):
            e = os.path.join(path, p)
            if os.path.isdir(e) and not (e.endswith("_slug") or e.endswith("_id")):
                # recursion
                routes.extend(self.get_nuxt_routes(e))
            elif e.endswith("_slug") or e.endswith("_id"):
                if "projects" in e:
                    routes.extend(self._generate_details_routes(e, Project))
                elif "christmas" in e:
                    routes.extend(self._generate_details_routes(e, Product))
            elif os.path.isfile(e) and e.endswith(".vue"):
                if e.endswith("index.vue"):
                    route = e[:-9].replace(self._path, "")
                    if not route == "/":
                        route = route[:-1]
                else:
                    route = e[:-4].replace(self._path, "")
                route = self._adjust_route(route)
                routes.append(route)
        return routes

    def _generate_details_routes(self, route, _class):
        list_name = os.path.basename(os.path.dirname(route))
        objects = _class.objects.all()
        #if list_name == f"{_class.__name__.lower()}s":
        routes_list = [
            self._adjust_route(f"/{list_name}/{p.slug_it}") for p in objects
        ]
        routes_list.extend([
            self._adjust_route(f"/{list_name}/{p.slug_en}") for p in objects
        ])
        return routes_list

    def _adjust_route(self, route):
        if route.count("/") > 1:
            count = route.count("/")
            route = route.replace("/", "--")
            route = route.replace("--", "/", count - 1)
        return route


class PageUtils:

    def __init__(self, path):
        self._path = path


class LayoutUtils(PageUtils):

    def get_layouts(self, nested_path=None):
        path = nested_path if nested_path else self._path
        layouts = []
        for sl in os.listdir(path):
            e = os.path.join(path, sl)
            if os.path.isfile(e) and sl.endswith(".vue"):
                layouts.append(sl[:-4])
            elif os.path.isdir(e):
                layouts.extend(self.get_layouts(e))
        return layouts


class ButtonUtils(PageUtils):

    def get_icons(self, nested_path=None):
        path = nested_path if nested_path else self._path
        icons = []
        for icon in os.listdir(path):
            e = os.path.join(path, icon)
            if os.path.isfile(e):
                icon_name = icon[:-4]
                icons.append((icon_name, icon_name))
            elif os.path.isdir(e):
                icons.extend(self.get_icons(e))
        return icons


if __name__ == "__main__":
    # Test pages
    ru = RoutingUtils("../../frontend/pages")
    routes = ru.get_nuxt_routes()
    print(routes)
    # Test layouts
    lu = LayoutUtils("../../frontend/components/sections")
    layouts = lu.get_layouts()
    print(layouts)
