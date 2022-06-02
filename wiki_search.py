from collections import deque
import sys
sys.setrecursionlimit(100000)

def main():
  pages = {}
  links = {}

  with open('data/pages.txt', encoding="utf-8") as f:
    for data in f.read().splitlines():
      page = data.split('\t')
      # page[0]: id, page[1]: title
      pages[page[0]] = page[1]

  with open('data/links.txt', encoding="utf-8") as f:
    for data in f.read().splitlines():
      link = data.split('\t')
      # link[0]: id (from), links[1]: id (to)
      if link[0] in links:
        links[link[0]].add(link[1])
      else:
        links[link[0]] = {link[1]}
    #print(links)
  
  start_name = input('start page name: ')
  goal_name = input('goal page name: ')
  for k, v in pages.items():
    if v == start_name:
      print(start_name, k)
      start_id = k
    elif v == goal_name:
      print(goal_name, k)
      goal_id = k
  
  print('*searching result by dfs')
  print(dfs(links, start_id, goal_id))
  print('*searching result by bfs')
  print(bfs(links, start_id, goal_id))


def dfs(node, start, target):
  stack = deque()
  stack.append(start)
  visited = {} #一度訪れたところを記録する
  visited[start] = True
  path = [] #道順を記録するリスト
  path.append(start)

  while stack:
    v = stack.pop()
    if v == target:
      path.append(v)
      return True
    
    if v in node:
      for follow in node[v]:
        if not follow in visited:
          visited[follow] = True
          stack.append(follow)
          path.append(follow)
          #print(visited)
          #print(stack)
          #print(path)

  return False

def bfs(node, start, target):
  stack = deque()
  stack.append(start)
  visited = {}
  visited[start] = True
  path = []
  path.append(start)

  while stack:
    v = stack.popleft()
    if v == target:
      path.append(v)
      return True
    
    if v in node:
      for follow in node[v]:
        if not follow in visited:
          visited[follow] = True
          stack.append(follow)
          path.append(follow)
          #print(visited)
          #print(stack)
          #print(path)
          
  return False


if __name__ == '__main__':
  main()
