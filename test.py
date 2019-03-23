# from keras.models import Sequential
# from keras.layers import Dense, Activation
#
# model = Sequential([
#     Dense(32, input_shape=(784,)),
#     Activation('relu'),
#     Dense(10),
#     Activation('softmax'),
# ])
#
# print ('66')
# i = 0
# m = 10000
# for n in range(2, m, 7):
#         if n % 5 == 3:
#             if n % 3 == 2:
#                 print'%d' % n
#                 i = i+1
#
# print '%d in 1-%d satisfied' % (i, m)

# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L =[1] + [L[n] + L[n-1] for n in range(1,len(L))] + [1]
#
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break
t = 0
print(range(300, 401, 2))
for i in range(300, 401, 2):
    t = t + i

print(t)
c = 200 * 201 - 149 * 150
print(c)
